import React from 'react'

interface Props {
    children: string;
    //color?: 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info' | 'light' | 'dark';
    onClick: () => void;
}

// { children, onClick, color = 'primary' }: Props

const Button = ({ children, onClick }: Props) => {
  return (
    <button className = 'btn btn-primary' onClick = {onClick}>{children}</button>
  )
}

export default Button
