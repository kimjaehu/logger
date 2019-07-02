import { GET_RESUME, DELETE_RESUME, ADD_RESUME } from '../actions/types.js';

const initialState = {
  resume: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_RESUME:
      return {
        ...state,
        resume: action.payload
      };
    case DELETE_RESUME:
      return {
        ...state,
        resume: state.resume.filter(each => each.id !== action.payload)
      };
    case ADD_RESUME:
      return {
        ...state,
        resume: [...state.resume, action.payload]
      };
    default:
      return state;
  }
}
