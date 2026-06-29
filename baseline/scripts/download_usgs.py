import os
import argparse
import tarfile
import glob
import shutil
from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

def download_and_extract_scenes(username, password, latitude, longitude, start_date, end_date, max_cloud, output_dir):
    # Initialize API
    print("Connecting to USGS EarthExplorer API...")
    api = API(username, password)
    
    # Landsat 8-9 OLI/TIRS Collection 2 Level 2 dataset
    dataset = 'LANDSAT_OT_C2_L2'
    
    print(f"Searching for Landsat 9 scenes (dataset: {dataset}) near Lat: {latitude}, Lon: {longitude}...")
    scenes = api.search(
        dataset=dataset,
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date,
        max_cloud_cover=max_cloud
    )
    
    print(f"Found {len(scenes)} matching scenes.")
    
    # Filter for Landsat 9 scenes (they start with LC09)
    l9_scenes = [s for s in scenes if s['display_id'].startswith('LC09')]
    print(f"Filtered to {len(l9_scenes)} Landsat 9 scenes.")
    
    if not l9_scenes:
        print("No Landsat 9 scenes found. Exiting.")
        api.logout()
        return
    
    # Limit downloading to prevent taking up excessive space/time
    # User can adjust this or specify a count limit
    limit = 3
    to_download = l9_scenes[:limit]
    print(f"Preparing to download the top {len(to_download)} scenes.")
    
    os.makedirs(output_dir, exist_ok=True)
    temp_download_dir = os.path.join(output_dir, 'temp_downloads')
    os.makedirs(temp_download_dir, exist_ok=True)
    
    ee = EarthExplorer(username, password)
    
    for scene in to_download:
        scene_id = scene['display_id']
        entity_id = scene['entity_id']
        print(f"\n--- Processing Scene: {scene_id} ---")
        
        # Download
        tar_path = os.path.join(temp_download_dir, f"{scene_id}.tar")
        if not os.path.exists(tar_path):
            print(f"Downloading {scene_id}...")
            try:
                ee.download(entity_id, output_dir=temp_download_dir)
                # landsatxplore downloads files named after the entity ID or scene ID, let's find it
                downloaded_files = glob.glob(os.path.join(temp_download_dir, f"*{entity_id}*")) + \
                                   glob.glob(os.path.join(temp_download_dir, f"*{scene_id}*"))
                if downloaded_files:
                    tar_path = downloaded_files[0]
                else:
                    print(f"Warning: Could not find downloaded file for {scene_id}")
                    continue
            except Exception as e:
                print(f"Error downloading {scene_id}: {e}")
                continue
        else:
            print(f"Tar file for {scene_id} already exists locally.")
            
        # Target folder for extracted bands
        target_scene_dir = os.path.join(output_dir, scene_id)
        os.makedirs(target_scene_dir, exist_ok=True)
        
        print(f"Extracting required bands from {tar_path}...")
        try:
            with tarfile.open(tar_path, 'r') as tar:
                # We only need B2, B3, B4, and B10
                for member in tar.getmembers():
                    if any(suffix in member.name for suffix in ['_B2.TIF', '_B3.TIF', '_B4.TIF', '_B10.TIF']):
                        # Extract this file
                        tar.extract(member, path=target_scene_dir)
                        print(f"  Extracted: {member.name}")
            
            # Remove the temp downloaded archive to save space
            os.remove(tar_path)
            print(f"Cleaned up temp archive: {tar_path}")
        except Exception as e:
            print(f"Error extracting {tar_path}: {e}")
            
    # Cleanup
    try:
        shutil.rmtree(temp_download_dir)
    except Exception:
        pass
        
    api.logout()
    ee.logout()
    print("\nDataset acquisition completed!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='USGS EarthExplorer Landsat 9 Downloader')
    parser.add_argument('--username', type=str, required=True, help='USGS EarthExplorer username')
    parser.add_argument('--password', type=str, required=True, help='USGS EarthExplorer password')
    parser.add_argument('--lat', type=float, default=28.61, help='Latitude for search center (default: Delhi 28.61)')
    parser.add_argument('--lon', type=float, default=77.23, help='Longitude for search center (default: Delhi 77.23)')
    parser.add_argument('--start', type=str, default='2023-01-01', help='Start date YYYY-MM-DD')
    parser.add_argument('--end', type=str, default='2023-12-31', help='End date YYYY-MM-DD')
    parser.add_argument('--max_cloud', type=int, default=10, help='Maximum cloud cover percentage')
    parser.add_argument('--output_dir', type=str, default='input', help='Target directory for scenes')
    
    args = parser.parse_args()
    
    # Resolve output directory relative to baseline
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, args.output_dir)
    
    download_and_extract_scenes(
        args.username, args.password,
        args.lat, args.lon,
        args.start, args.end,
        args.max_cloud, output_path
    )
