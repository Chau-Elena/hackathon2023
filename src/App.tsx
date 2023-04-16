import React, { useState, ChangeEvent } from "react";
import NumberInput from "./components/NumberInput";
import "./styles/NumberInput.css";

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
    </div>
  );
}

export default App;
