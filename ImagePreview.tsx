import React from 'react';

interface Props {
  previewUrl: string;
}

function ImagePreview(props: Props) {
  return (
    <div>
      {props.previewUrl && <img src={props.previewUrl} alt="Preview" />}
    </div>
  );
}

export default ImagePreview;
