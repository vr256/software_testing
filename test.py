import behave.__main__

if __name__ == '__main__':
    behave.__main__.main(["-i", "upload_file.feature"])
    behave.__main__.main(["-i", "get_file_metadata.feature"])
    behave.__main__.main(["-i", "delete_file.feature"])