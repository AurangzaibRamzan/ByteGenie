"use client";
import React, { useState } from 'react';
import Layout from '@/app/components/Layout';
import ResultsTable from '@/app/components/ResultsTable';
import SearchField from '@/app/components/SearchField';
import { fetchQueryResults } from '@/utils/api';

const Home = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [noResults, setNoResults] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    setNoResults(false);
    try {
      const { result, status } = await fetchQueryResults(query);
      if (result.length === 0) {
        setNoResults(true);
      } else {
        setResults(result);
      }
    } catch (error) {
      setError("Error fetching data");
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <SearchField query={query} setQuery={setQuery} handleSearch={handleSearch} />
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {noResults && <p>No results found</p>}
      {results.length > 0 && <ResultsTable results={results} />}
    </Layout>
  );
};

export default Home;
