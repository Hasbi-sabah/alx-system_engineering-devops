File Transfer Using SFTP

1. Open a terminal or command prompt on your local machine.

2. Establish an SFTP connection to the sandbox environment by using the following command: *sftp username@hostname*. Replace "username" with your actual username and "hostname" with the appropriate hostname or IP address for the sandbox environment.

3. Enter your password when prompted to authenticate and establish the SFTP connection.

4. Navigate to the directory on the sandbox environment where you want to upload the screenshots using the cd command. For example: *cd /path/to/sandbox/directory*.
5. Use the put command to upload the screenshots from your local machine to the sandbox environment. Provide the full path to each screenshot file you want to upload. For example:

*put /Users/YourUsername/folder/screenshot1.png*

*put /Users/YourUsername/folder/screenshot2.png*

*put /Users/YourUsername/folder/screenshot3.png*

Replace "/Users/YourUsername/folder/YourFile.png" with the actual path and filename of each screenshot you want to upload.

6. To confirm the successful transfer of the screenshots, check the contents of the sandbox directory using the ls command: *ls*. This will display a list of files in the current directory on the sandbox environment, including the uploaded screenshots.

7. When you have finished transferring and verifying the screenshots, you can exit the SFTP session using the quit or exit command: *quit*.

By following these steps, you should be able to upload the screenshots from your local machine to the sandbox environment using SFTP and confirm that the transfer was successful.
