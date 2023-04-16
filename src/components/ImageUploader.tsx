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
