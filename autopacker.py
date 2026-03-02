import shutil
from pathlib import Path

def create_vehicle_pack():
    # get user inputs
    input_dir = input("Path to the directory containing vehicle resources: ").strip()
    pack_name = input("Name for the vehicle pack: ").strip()
    description = input("Description for the vehicle pack: ").strip()

    # check if the dir exists
    input_path = Path(input_dir)
    if not input_path.is_dir():
        print("Error: The provided input path is not a directory.")
        return

    # sanitise pack name and escape description quotes
    pack_name = pack_name.replace(' ', '_')
    description = description.replace("'", "\\'")

    # create pack dir inside 'input_dir'
    pack_dir = input_path / pack_name
    pack_dir.mkdir(exist_ok=True)

    # create stream and data folders inside the pack dir
    stream_dir = pack_dir / 'stream'
    stream_dir.mkdir(exist_ok=True)
    data_dir = pack_dir / 'data'
    data_dir.mkdir(exist_ok=True)

    # find sub dirs in 'input_dir' (assuming each is a vehicle resource)
    for resource_path in input_path.iterdir():
        if resource_path.is_dir() and resource_path != pack_dir:
            resource_name = resource_path.name

            # create sub folders inside the stream and data folders with the vehicle resource name
            resource_stream_dir = stream_dir / resource_name
            resource_stream_dir.mkdir(exist_ok=True)
            resource_data_dir = data_dir / resource_name
            resource_data_dir.mkdir(exist_ok=True)

            # copy all the srteam files to the sub folder in stream dir
            source_stream = resource_path / 'stream'
            if source_stream.exists():
                for file_path in source_stream.glob('*.*'):
                    if file_path.is_file():
                        shutil.copy(file_path, resource_stream_dir / file_path.name)
            else:
                print(f"  Warning: no stream folder found in {resource_name}")

            # copy all .meta files to the sub folder in data dir
            meta_files = list(resource_path.glob('*.meta'))
            if not meta_files:
                print(f"  Warning: no .meta files found in {resource_name}")
            for meta_file in meta_files:
                if meta_file.is_file():
                    shutil.copy(meta_file, resource_data_dir / meta_file.name)

    # create fxmanifest with the description (should have all the required data_files, create an issue in the github repo if theres one missing)
    fxmanifest_content = f"""fx_version 'cerulean'
game 'gta5'
lua54 'yes'
description '{description}'

files {{
    'data/**/*.meta',
    'stream/**/*.*',
}}

data_file 'CONTENT_UNLOCKING_META_FILE' 'data/**/contentunlocks.meta'
data_file 'HANDLING_FILE' 'data/**/handling.meta'
data_file 'VEHICLE_METADATA_FILE' 'data/**/vehicles.meta'
data_file 'CARCOLS_FILE' 'data/**/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/**/carvariations.meta'
data_file 'VEHICLE_LAYOUTS_FILE' 'data/**/vehiclelayouts.meta'
"""

    # write to the file
    fxmanifest_path = pack_dir / 'fxmanifest.lua'
    with open(fxmanifest_path, 'w') as f:
        f.write(fxmanifest_content)

    # cba to error check so enjoy :)
    print(f"Vehicle Pack Created: {pack_dir}")

if __name__ == "__main__":
    create_vehicle_pack()