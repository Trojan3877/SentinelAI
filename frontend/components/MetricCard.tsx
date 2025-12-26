type Props = {
  title: string;
  value: string;
};

export default function MetricCard({ title, value }: Props) {
  return (
    <div className="rounded-xl bg-gray-900 p-4 text-white shadow">
      <h3 className="text-sm text-gray-400">{title}</h3>
      <p className="text-2xl font-bold">{value}</p>
    </div>
  );
}
