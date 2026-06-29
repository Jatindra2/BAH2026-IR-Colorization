import os
import argparse
import tarfile
import glob
import re

def clean_product_id(filename):
    # Remove file extension and any trailing space + (1), (2), etc.
    name = os.path.splitext(filename)[0]
    name = re.sub(r'\s*\(\d+\)$', '', name)
    return name

def extract_bands(dataset_dir, output_root, limit=None):
    tar_pattern = os.path.join(dataset_dir, "*.tar")
    tar_files = glob.glob(tar_pattern)
    
    # Filter for files larger than 10MB to skip empty or corrupt downloads
    valid_tars = []
    for f in tar_files:
        if os.path.getsize(f) > 10 * 1024 * 1024:
            valid_tars.append(f)
            
    print(f"Found {len(tar_files)} total tar files. {len(valid_tars)} are valid (size > 10MB).")
    
    if limit:
        valid_tars = valid_tars[:limit]
        print(f"Limiting extraction to {len(valid_tars)} scenes.")
        
    extracted_count = 0
    
    # Define mapping of bands we want to extract
    band_map = {
        'SR_B2.TIF': 'B2.TIF',
        'SR_B3.TIF': 'B3.TIF',
        'SR_B4.TIF': 'B4.TIF',
        'ST_B10.TIF': 'B10.TIF'
    }
    
    for tar_path in valid_tars:
        filename = os.path.basename(tar_path)
        product_id = clean_product_id(filename)
        
        target_dir = os.path.join(output_root, product_id)
        os.makedirs(target_dir, exist_ok=True)
        
        print(f"\nExtracting {filename} -> {product_id}...")
        
        # Check if all four files already exist (skip if already extracted)
        all_exist = True
        for dest_name in band_map.values():
            dest_path = os.path.join(target_dir, f"{product_id}_{dest_name}")
            if not os.path.exists(dest_path):
                all_exist = False
                break
                
        if all_exist:
            print("  All required bands already extracted. Skipping.")
            extracted_count += 1
            continue
            
        try:
            with tarfile.open(tar_path, 'r') as tar:
                members = tar.getmembers()
                extracted_bands = 0
                
                for member in members:
                    # Check if member matches one of our target bands
                    matched_band = None
                    for key in band_map.keys():
                        if member.name.endswith(key):
                            matched_band = key
                            break
                            
                    if matched_band:
                        # Set destination file name
                        dest_name = f"{product_id}_{band_map[matched_band]}"
                        dest_path = os.path.join(target_dir, dest_name)
                        
                        # Extract and rename
                        # Extract member file object
                        f_in = tar.extractfile(member)
                        if f_in:
                            with open(dest_path, 'wb') as f_out:
                                f_out.write(f_in.read())
                            print(f"  Extracted and renamed: {member.name} -> {dest_name}")
                            extracted_bands += 1
                            
                if extracted_bands == 4:
                    print(f"  Successfully extracted all 4 bands for {product_id}.")
                    extracted_count += 1
                else:
                    print(f"  Warning: Only extracted {extracted_bands}/4 bands for {product_id}.")
                    
        except Exception as e:
            print(f"  Error extracting tar file {tar_path}: {e}")
            
    print(f"\nExtraction completed! Successfully extracted {extracted_count} scenes.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract B2, B3, B4, B10 bands from Landsat tar archives")
    parser.add_argument('--dataset_dir', type=str, default='D:/Datasets', help='Path to directory containing downloaded tar files')
    parser.add_argument('--limit', type=int, default=None, help='Limit the number of scenes to extract')
    
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_input_dir = os.path.join(base_dir, 'input')
    
    # Run extraction
    extract_bands(args.dataset_dir, output_input_dir, limit=args.limit)
