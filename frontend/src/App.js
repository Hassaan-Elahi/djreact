import React, { Component } from 'react';
import 'antd/dist/antd.css';
import './App.css';
import CustomLayout from './containers/layout';

class App extends Component
{
  render()
  {
      return (
        <div className="App">
         <CustomLayout>

         </CustomLayout>
        </div>
      );
  }
}

export default App;
