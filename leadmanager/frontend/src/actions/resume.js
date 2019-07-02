import axios from 'axios';
import { createMessage, returnErrors } from './messages';
import { tokenConfig } from './auth';

import { GET_RESUME, DELETE_RESUME, ADD_RESUME } from './types';

// GET RESUME
export const getResume = () => (dispatch, getState) => {
  axios
    .get('/api/resumes/', tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_RESUME,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// DELETE RESUME
export const deleteResume = id => (dispatch, getState) => {
  axios
    .delete(`/api/resumes/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteResume: 'Working...' }));
      dispatch({
        type: DELETE_RESUME,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

// ADD RESUME
export const addResume = resume => (dispatch, getState) => {
  axios
    .post('/api/resumes/', resume, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addResume: 'Resume Saved' }));
      dispatch({
        type: ADD_RESUME,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
