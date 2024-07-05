import axios from 'axios';
import _ from 'lodash';

export const fetchQueryResults = async (query) => {
  try {
    const response = await axios.post('http://localhost:8888/query-maker', { text: query });
    console.log(response);
    return {result:_.get(response,'data.data',[]),status: _.get(response,'status')};
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};
