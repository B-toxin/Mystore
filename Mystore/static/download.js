let currentIndex = 0;

function downloadFile(index) {
    // Use the current index to request the next file
    $.ajax({
        url: `/get_next_file/${index}`,
        success: function () {
            currentIndex++;
            if (currentIndex < {{ total_number_of_files }}) { // Replace with the total number of files
                // Update the download link with the new index
                document.getElementById('downloadButton').setAttribute('onclick', `downloadFile(${currentIndex})`);
            } else {
                // All files have been downloaded
                document.getElementById('downloadButton').innerHTML = "No more files to download";
                document.getElementById('downloadButton').setAttribute('onclick', '');
            }
        },
        error: function () {
            console.error("Error downloading file.");
        }
    });
}
