import React, { ChangeEvent, FC } from 'react';

type NumberInputProps = {
  id: string;
  label: string;
  value: number;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
}

const NumberInput: FC<NumberInputProps> = ({ id, label, value, onChange }) => {
  return (
    <div className="number-input">
      <label htmlFor={id}>{label}</label>
      <input
        type="number"
        id={id}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}

export default NumberInput;
