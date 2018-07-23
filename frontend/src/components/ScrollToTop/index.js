import { Component } from 'react';
import { withRouter } from 'react-router-dom';

// This component helps with redirecting - by default after redirection the browser saves the scroll position
// So we have to tell it, that after changing of location it should go to top of the page

class ScrollToTop extends Component {
  componentDidUpdate(prevProps) {
    if (this.props.location !== prevProps.location) {
      window.scrollTo(0, 0)
    }
  }

  render() {
    return this.props.children
  }
}

export default withRouter(ScrollToTop)