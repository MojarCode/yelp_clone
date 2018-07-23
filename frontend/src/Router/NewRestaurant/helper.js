export const validate_form = (state) => {
  return Object.keys(state).filter(property => {
    return state[property].trim() === '';
  })
}