//import Message from './Message'; //'.' means current directory

import React, { ReactNode } from "react";
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

  return (
    <div>
      <HomePage />
      <Button onClick={() => console.log('Clicked')}>My Button</Button>
    </div>
  );
}

export default App;
