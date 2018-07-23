import { setTokens } from './userActions';

export const fetchLocalUser = () => (dispatch, getState) => {
  const tokensStr = localStorage.getItem('tokens');
  if (tokensStr) {
    const tokens = JSON.parse(tokensStr);
    dispatch(setTokens(tokens));
  }
}