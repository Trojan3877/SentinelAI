import axios from "axios";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface HealthResponse {
  status: string;
}

export const getHealth = async (): Promise<HealthResponse> => {
  const res = await axios.get(`${API_BASE}/health`);
  return res.data;
};
