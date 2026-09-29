// Client-side interactions for Drag & Drop and Image Preview
document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const formFileInput = document.getElementById('form-file-input');
    const btnUpload = document.getElementById('btn-upload');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const fileName = document.getElementById('file-name');
    const fileSize = document.getElementById('file-size');
    const dropText = document.getElementById('drop-text');
    const dropIcon = document.getElementById('drop-icon');

    if (!dropZone || !fileInput) return;

    // Handle drag over
    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add('dragover');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove('dragover');
        }, false);
    });

    // Handle dropped files
    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    });

    // Handle click file selection
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });

    function handleFileSelect(file) {
        // Client-side validation
        const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/bmp'];
        if (!validTypes.includes(file.type)) {
            alert('Unsupported file type. Please upload JPG, PNG, WEBP, or BMP.');
            return;
        }

        const maxMB = 10;
        if (file.size > maxMB * 1024 * 1024) {
            alert(`File too large (${(file.size / (1024*1024)).toFixed(1)} MB). Max limit is ${maxMB} MB.`);
            return;
        }

        // Set file into hidden form input
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        formFileInput.files = dataTransfer.files;

        // Render Preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            previewContainer.style.display = 'flex';
            if (dropText) dropText.style.display = 'none';
            if (dropIcon) dropIcon.style.display = 'none';

            fileName.textContent = file.name;
            fileSize.textContent = `(${(file.size / 1024).toFixed(1)} KB)`;
            btnUpload.disabled = false;
        };
        reader.readAsDataURL(file);
    }
});
