import React from 'react'

const App = () => {
  ReactDOM.createRoot(document.getElementById("root")).render(element);
  return (
    <div>
      const element =(
        <h1>Hello ruhith</h1>
        <h2>The time is {new Date().toLocaleTimeString()}.</h2>
      )
    </div>
  )
}
setInterval(App, 1000)

export default App
