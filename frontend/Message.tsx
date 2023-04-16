
//PascalCasing
function Message() {
    // JSX: JavaScript XML
    const name  = 'Elena';
    if (name)
        return <h1>Hello {name}</h1>;
    return <h1>Hello World</h1>;
}

// babeljs.io/repl [shows how the JSX is converted to JS]

export default Message;