export const initialState = {
  concepts: [],
  loading: false,
  error: null,
  storyboard: null,
  moodboard: null
};

export function appReducer(state, action) {
  switch (action.type) {
    case "GENERATE_CONCEPTS_START":
      return {
        ...state,
        loading: true,
        error: null
      };

    case "GENERATE_CONCEPTS_SUCCESS":
      return {
        ...state,
        loading: false,
        concepts: action.payload,
        error: null
      };

    case "GENERATE_CONCEPTS_ERROR":
      return {
        ...state,
        loading: false,
        error: action.payload
      };

    case "CLEAR_CONCEPTS":
      return {
        ...state,
        concepts: []
      };

    // Future actions
    case "SET_STORYBOARD":
      return {
        ...state,
        storyboard: action.payload
      };

    case "SET_MOODBOARD":
      return {
        ...state,
        moodboard: action.payload
      };

    default:
      return state;
  }
}
