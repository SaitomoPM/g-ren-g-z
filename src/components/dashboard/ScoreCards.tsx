import { TrendingUp, Hash, Target, BarChart } from "lucide-react";

const kpis = [
  {
    label: "Toplam GP",
    value: "87.4",
    icon: TrendingUp,
    borderColor: "border-l-saglik-success",
    delta: "+2.1",
    deltaUp: true,
  },
  {
    label: "Gösterge Sayısı",
    value: "42",
    icon: Hash,
    borderColor: "border-l-saglik-info",
    delta: "0",
    deltaUp: null,
  },
  {
    label: "Başarı Oranı",
    value: "%78.5",
    icon: Target,
    borderColor: "border-l-saglik-success",
    delta: "+4.2%",
    deltaUp: true,
  },
  {
    label: "GD Ortalaması",
    value: "3.28",
    icon: BarChart,
    borderColor: "border-l-saglik-warning",
    delta: "-0.15",
    deltaUp: false,
  },
];

const ScoreCards = () => {
  return (
    <section>
      <h2 className="saglik-section-title">2026 Ocak-Mart Dönemi Performans Özeti</h2>
      <p className="saglik-section-desc">Seçili dönem için temel performans göstergeleri</p>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {kpis.map((kpi) => {
          const Icon = kpi.icon;
          return (
            <div key={kpi.label} className={`saglik-kpi-card ${kpi.borderColor}`}>
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm text-muted-foreground">{kpi.label}</span>
                <Icon className="w-5 h-5 text-muted-foreground" />
              </div>
              <div className="text-2xl font-bold text-foreground">{kpi.value}</div>
              {kpi.deltaUp !== null && (
                <div className={`text-xs mt-1 font-medium ${kpi.deltaUp ? "text-saglik-success" : "text-saglik-warning"}`}>
                  {kpi.delta} önceki döneme göre
                </div>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
};

export default ScoreCards;
