import shutil
import argparse
import time


def sync_folders(source_folder, replica_folder, log_file, sync_interval):
    while True:
        # Perform synchronization.
        synchronize(source_folder, replica_folder, log_file)
        time.sleep(sync_interval)


def synchronize(source_folder, replica_folder, log_file):
    # Synchronizes the source folder with the replica folder.
    try:
        shutil.rmtree(replica_folder)
        shutil.copytree(source_folder, replica_folder)
        log_operation(log_file, "Synchronization successful.")
    except Exception as e:
        log_operation(log_file, f"Error: {e}")


def log_operation(log_file, operation):
    with open(log_file, 'a') as log:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log.write(f"{timestamp} - {operation}\n")


def main():
    parser = argparse.ArgumentParser(description='Synchronize folders.')
    parser.add_argument('source_folder', help='Source folder path')
    parser.add_argument('replica_folder', help='Replica folder path')
    parser.add_argument('log_file', help='Log file path')
    parser.add_argument('sync_interval', type=int, help='Sync interval in seconds')
    args = parser.parse_args()

    sync_folders(args.source_folder, args.replica_folder, args.log_file, args.sync_interval)


if __name__ == '__main__':
    main()
