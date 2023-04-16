import { Fragment, useState } from "react";
// import { MouseEvent } from "react";

// {items: [], heading: string}
interface Props {
  items: string[];
  heading: string;
  //(item: string) => void
  onSelectItem: (item: string) => void; //onClick
}

function ListGroup({ items, heading, onSelectItem }: Props) {
  //return <h1>List Group</h1>;
  const [selectedIndex, setSelectedIndex] = useState(-1);

  heading = "";

  //   arr[0] //variable (selectedIndex)
  //   arr[1] //updater function

  // Event handler
  //   const handleClick = (event: MouseEvent) => console.log(event);
  //   //items = [];

  //   if (items.length == 0)
  //     return (
  //       <>
  //         <h1>List</h1>
  //         <p>There are no items in the list.</p>
  //       </>
  //     );

  //const message = items.length === 0 ? <p>There are no items in the list.</p> : null;

  //   const getMessage = () => {
  //     return items.length === 0 ? <p>There are no items in the list.</p> : null;
  //   }

  return (
    <>
      <h1>{heading}</h1>
      {items.length == 0 && <p>There are no items in the list.</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;

//cmd + p: search for file
//cmd + d: select next instance of the same word
