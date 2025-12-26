"use client";

import { useEffect, useState } from "react";
import { getHealth } from "../../lib/api";
import MetricCard from "../../components/MetricCard";

export default function Dashboard() {
  const [status, setStatus] = useState("Loading...");

  useEffect(() => {
    getHealth().then(res => setStatus(res.status));
  }, []);

  return (
    <div className="grid grid-cols-3 gap-4">
      <MetricCard title="API Status" value={status} />
      <MetricCard title="LLM" value="Llama 3 (CUDA)" />
      <MetricCard title="CI/CD" value="Healthy" />
    </div>
  );
}
