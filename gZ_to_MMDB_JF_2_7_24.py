import tarfile

# Create free Maxmind account to gain access to geoIP2 files
# Navigate to left rail then GeoIP2/GeoLite2 and then Download Files
# Download Gzip from https://www.maxmind.com/en/accounts/970463/geoip/downloads
# Replace with your .tar.gz file path

input_tar_gz_file = 'path to your .gz file for extraction' # input directory
output_directory = 'path/to/your/output'  # output directory will populate in mmdb file type

with tarfile.open(input_tar_gz_file, 'r:gz') as tar:
    for member in tar.getmembers():
        if member.name.endswith('.mmdb'):
            tar.extract(member, output_directory)