import React, { Component } from "react";
import logo from './logo.png'

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src={logo}
          width="300"
          //className="img-thumbnail"
          style={{ marginTop: "10px" }}
        />
        <hr />
      </div>
    );
  }
}

export default Header;