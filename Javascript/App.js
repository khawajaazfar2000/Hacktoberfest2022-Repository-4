import logo from './logo.svg';
import './App.css';
import Header from './Header';
import Home from './Home';
import Sale from './Sale';
import Footer from './Footer';
import Unstitched from './Unstitched';
import { BrowserRouter,Link,Switch,Route } from 'react-router-dom';

function App() {
  return (
    <>
      <BrowserRouter>
      <Header />
      <Switch>
        <Route exact path = "/home">
      <Home />
      </Route>
      <Route path = "/sale">
      <Sale />
      </Route>
      <Route path = "/unstitched">
      <Unstitched />
      </Route>
      </Switch>
      <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
