import React from "react";
import ImagePreview from "./ImagePreview";

function ImageUploader() {
  const [previewUrl, setPreviewUrl] = React.useState("");

  function handleFileInputChange(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setPreviewUrl(reader.result as string);
      };
      reader.readAsDataURL(file);
    } else {
      setPreviewUrl("");
    }
  }

  function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    // Add code to upload the file to the backend
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
    const file = fileInput.files?.[0];
    if (file) {
      const formData = new FormData();
      formData.append("image", file);

      fetch("/upload", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          console.log("image received image successfully   ");
          // handle response
        })
        .catch((error) => {
          console.log("image received image error")
          // handle error
        });
    }


  }

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <label>
          Select an image:
          <input
            type="file"
            accept="image/*"
            onChange={handleFileInputChange}
          />
        </label>
        <ImagePreview previewUrl={previewUrl} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default ImageUploader;
