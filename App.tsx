import React, { useState, ChangeEvent } from "react";
import axios from "axios";
import NumberInput from "./components/NumberInput";
import logo from './logo.svg';
import './App.css';
import "./styles/NumberInput.css";
import ImageUploader from './components/ImageUploader';

//----

//import Message from './Message'; //'.' means current directory
import HomePage from "./components/HomePage";

//import ListGroup from "./components/ListGroup";
// import Alert from "./components/Alert";
import Button from "./components/Button";

function App() {
  // let items = ["New York", "San Francisco", "Tokyo", "London", "Paris"];

  // const handleSelectItem = (item: string) => {
  //   console.log(item);
  // }

  //const [alertVisible, setAlertVisibility] = useState(false);

  axios({
    method: "GET",
    url:"/profile",
  })
  .then((response) => {
    const res =response.data
    setProfileData(({
      profile_name: res.name,
      about_me: res.about}))
  }).catch((error) => {
    if (error.response) {
      console.log(error.response)
      console.log(error.response.status)
      console.log(error.response.headers)
      }
  })}

  const [number, setNumber] = useState<number>(0);

  const handleNumberChange = (event: ChangeEvent<HTMLInputElement>) => {
    setNumber(parseInt(event.target.value));
  };

  return (
    <div className="App">
      <HomePage />
      <Button onClick={() => console.log("Clicked")}>My Button</Button>
      <NumberInput
        id="number-input"
        label="Enter a number:"
        value={number}
        onChange={handleNumberChange}
      />

      <h1>Image Uploader</h1>
      <ImageUploader />
    </div>
  );
}

export default App;

// ---
