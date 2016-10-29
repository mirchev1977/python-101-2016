import sys
import os


def main():
    path = sys.argv[1]

    total_bytes = 0
    for root, subdirs, files in os.walk(path):
        for file in files:
            total_bytes += os.path.getsize(os.path.join(root, file))

    into_gygabytes = total_bytes / 1000000000
    print(into_gygabytes)


if __name__ == "__main__":
    main()
    
