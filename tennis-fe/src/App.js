import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import bimg from './gt.jpeg'
class App extends Component {
  render() {
    return (
      
      
      <Fragment >
        
        <div style={{
        backgroundImage: `url(${bimg})`}}>
        <Header />
        
        <Home />
        </div>
      </Fragment>
     
    );
  }
}

export default App;