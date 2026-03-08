import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine, Legend, Cell
} from "recharts";
import { AlertTriangle, TrendingUp } from "lucide-react";

const trendData = [
  { month: "Eki", value: 72, target: 80, achieved: false },
  { month: "Kas", value: 75, target: 80, achieved: false },
  { month: "Ara", value: 81, target: 80, achieved: true },
  { month: "Oca", value: 78, target: 80, achieved: false },
  { month: "Şub", value: 83, target: 80, achieved: true },
  { month: "Mar", value: 85, target: 80, achieved: true },
  { month: "Nis*", value: 84, target: 80, achieved: true },
  { month: "May*", value: 86, target: 80, achieved: true },
  { month: "Haz*", value: 87, target: 80, achieved: true },
];

const distributionData = [
  { name: "Ankara Şehir Hst.", value: 92, color: "#55BAB7" },
  { name: "Ankara EAH", value: 85, color: "#55BAB7" },
  { name: "Dr. Sami Ulus", value: 78, color: "#F59E0B" },
  { name: "Keçiören ADSM", value: 65, color: "#AF3C4E" },
  { name: "Altındağ ADSM", value: 58, color: "#AF3C4E" },
];

const parameterData = [
  { month: "Eki", numerator: 1250, denominator: 1500 },
  { month: "Kas", numerator: 1300, denominator: 1520 },
  { month: "Ara", numerator: 1400, denominator: 1480 },
  { month: "Oca", numerator: 1350, denominator: 1510 },
  { month: "Şub", numerator: 1420, denominator: 1490 },
  { month: "Mar", numerator: 1460, denominator: 1500 },
];

const anomalies = [
  { indicator: "Acil Servis Bekleme Süresi", zScore: 2.8, period: "Şubat 2026", severity: "Yüksek" },
  { indicator: "Lab Sonuç Süresi", zScore: 2.3, period: "Mart 2026", severity: "Orta" },
];

const predictions = [
  { period: "Nisan 2026", indicator: "Yatak Doluluk", risk: "Yüksek", message: "Hedef altında kalma riski %72" },
  { period: "Mayıs 2026", indicator: "Ameliyat İptal", risk: "Orta", message: "Artış eğilimi devam edebilir" },
  { period: "Haziran 2026", indicator: "Enfeksiyon Hızı", risk: "Düşük", message: "Stabil seyir bekleniyor" },
];

const ChartsSection = () => {
  return (
    <div className="space-y-6">
      {/* Trend Analysis */}
      <div className="saglik-card p-5">
        <h3 className="saglik-section-title">Gösterge Trend Analizi ve Tahmin</h3>
        <p className="saglik-section-desc">Son 6 aylık gerçekleşme ve 3 aylık tahmin (* ile işaretli)</p>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={trendData}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(210, 18%, 88%)" />
            <XAxis dataKey="month" tick={{ fontSize: 13 }} />
            <YAxis tick={{ fontSize: 13 }} />
            <Tooltip />
            <ReferenceLine y={80} stroke="#AF3C4E" strokeDasharray="5 5" label="Hedef" />
            <Line
              type="monotone"
              dataKey="value"
              stroke="#0095C6"
              strokeWidth={2}
              dot={({ cx, cy, payload }: any) => (
                <circle
                  key={payload.month}
                  cx={cx}
                  cy={cy}
                  r={5}
                  fill={payload.achieved ? "#55BAB7" : "#DC0D15"}
                  stroke="white"
                  strokeWidth={2}
                />
              )}
            />
            <Legend formatter={() => "Gerçekleşme / Tahmin"} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Distribution Analysis */}
      <div className="saglik-card p-5">
        <h3 className="saglik-section-title">Gösterge Dağılım Analizi</h3>
        <p className="saglik-section-desc">Hastaneler arası karşılaştırmalı performans dağılımı</p>
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={distributionData} layout="vertical" margin={{ left: 120 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(210, 18%, 88%)" />
            <XAxis type="number" domain={[0, 100]} tick={{ fontSize: 13 }} />
            <YAxis type="category" dataKey="name" tick={{ fontSize: 13 }} width={110} />
            <Tooltip />
            <Bar dataKey="value" radius={[0, 4, 4, 0]} barSize={24}>
              {distributionData.map((entry, index) => (
                <Cell key={index} fill={entry.color} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Critical Parameter Trend */}
      <div className="saglik-card p-5">
        <h3 className="saglik-section-title">Kritik Parametre Trendi</h3>
        <p className="saglik-section-desc">Alt parametrelerin (pay/payda) aylık seyri</p>
        <ResponsiveContainer width="100%" height={280}>
          <LineChart data={parameterData}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(210, 18%, 88%)" />
            <XAxis dataKey="month" tick={{ fontSize: 13 }} />
            <YAxis tick={{ fontSize: 13 }} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="numerator" stroke="#55BAB7" strokeWidth={2} name="Pay" dot={{ r: 3 }} />
            <Line type="monotone" dataKey="denominator" stroke="#0095C6" strokeWidth={2} name="Payda" dot={{ r: 3 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Anomaly Detection */}
      <div className="saglik-card p-5">
        <h3 className="saglik-section-title flex items-center gap-2">
          <AlertTriangle className="w-5 h-5 text-saglik-threat" />
          Anomali Tespiti
        </h3>
        <p className="saglik-section-desc">Z-skoru ile tespit edilen istatistiksel sapmalar</p>
        <div className="space-y-3">
          {anomalies.map((a) => (
            <div key={a.indicator} className="flex items-center justify-between p-3 rounded-lg bg-background border border-border">
              <div>
                <span className="font-medium text-sm">{a.indicator}</span>
                <span className="text-muted-foreground text-sm ml-2">({a.period})</span>
              </div>
              <div className="flex items-center gap-3">
                <span className="text-sm text-muted-foreground">Z: {a.zScore}</span>
                <span className={`text-xs font-medium px-2 py-0.5 rounded ${
                  a.severity === "Yüksek" ? "bg-saglik-threat text-primary-foreground" : "bg-saglik-warning text-primary-foreground"
                }`}>
                  {a.severity}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Predictive Alerts */}
      <div className="saglik-card p-5">
        <h3 className="saglik-section-title flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-saglik-info" />
          Tahmine Dayalı Uyarılar
        </h3>
        <p className="saglik-section-desc">Önümüzdeki 3 aylık dönem için öngörülen riskler</p>
        <div className="space-y-3">
          {predictions.map((p) => (
            <div key={p.period + p.indicator} className="flex items-center justify-between p-3 rounded-lg bg-background border border-border">
              <div>
                <span className="text-xs text-muted-foreground">{p.period}</span>
                <div className="font-medium text-sm">{p.indicator}</div>
                <div className="text-xs text-muted-foreground">{p.message}</div>
              </div>
              <span className={`text-xs font-medium px-2 py-0.5 rounded ${
                p.risk === "Yüksek" ? "bg-saglik-threat text-primary-foreground" :
                p.risk === "Orta" ? "bg-saglik-warning text-primary-foreground" :
                "bg-saglik-success text-primary-foreground"
              }`}>
                {p.risk}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ChartsSection;
