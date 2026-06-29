import os
import numpy as np
import tifffile

def generate_mock_landsat9_product(output_dir, product_id, size=(4000, 4000)):
    """Generates mock Landsat 9 TIF files for bands 2, 3, 4, and 10."""
    product_path = os.path.join(output_dir, product_id)
    os.makedirs(product_path, exist_ok=True)
    
    print(f"Generating mock data for product: {product_id} in {product_path}")
    
    # Generate uint16 data typical of Landsat Level 2 (scaled reflectance and temperature)
    # B2 (Blue), B3 (Green), B4 (Red) - typical range 0-65535, usually concentrated under 20000
    for band_name in ['_B2', '_B3', '_B4']:
        # Create some patterns (like horizontal/vertical gradients) so they look a bit like structure
        x = np.linspace(0, 10000, size[1])
        y = np.linspace(0, 10000, size[0])
        xv, yv = np.meshgrid(x, y)
        band_data = (xv + yv + np.random.randint(0, 2000, size)).astype(np.uint16)
        
        file_path = os.path.join(product_path, f"{product_id}{band_name}.TIF")
        tifffile.imwrite(file_path, band_data)
        print(f"  Created: {os.path.basename(file_path)}")

    # B10 (TIR) - typical values are kelvin * 10 or scaled values
    x = np.linspace(20000, 30000, size[1])
    y = np.linspace(30000, 20000, size[0])
    xv, yv = np.meshgrid(x, y)
    b10_data = (xv + yv + np.random.randint(0, 1000, size)).astype(np.uint16)
    
    file_path = os.path.join(product_path, f"{product_id}_B10.TIF")
    tifffile.imwrite(file_path, b10_data)
    print(f"  Created: {os.path.basename(file_path)}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_root = os.path.join(base_dir, 'input')
    
    # Create two mock products to have multiple samples
    generate_mock_landsat9_product(input_root, "LC09_L2SP_020030_20230615_20230623_02_T1")
    generate_mock_landsat9_product(input_root, "LC09_L2SP_020030_20230717_20230725_02_T1")
    print("Mock dataset generation completed successfully!")
