import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export const useScenario = (id) => {
  const { data, error, isLoading } = useSWR(
    `http://127.0.0.1:5000/api/getData?scenarioId=${id}`,
    fetcher,
    { refreshInterval: 500 }
  );

  return {
    scenario: data,
    isLoading,
    isError: error,
  };
};
