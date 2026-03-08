import { useState } from "react";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, Legend
} from "recharts";

const allHospitals = [
  "Ankara Şehir Hastanesi",
  "Ankara EAH",
  "Dr. Sami Ulus",
  "Keçiören ADSM",
  "Altındağ ADSM",
  "Çankaya ADSM",
  "Ankara ADSH",
  "Gölbaşı ADSH",
];

const comparisonData = [
  { name: "Hasta Memnuniyeti", "Ankara Şehir Hst.": 92, "Ankara EAH": 85, "Dr. Sami Ulus": 78 },
  { name: "Yatak Doluluk", "Ankara Şehir Hst.": 88, "Ankara EAH": 91, "Dr. Sami Ulus": 82 },
  { name: "Ameliyat İptal", "Ankara Şehir Hst.": 5, "Ankara EAH": 8, "Dr. Sami Ulus": 12 },
  { name: "Enfeksiyon Hızı", "Ankara Şehir Hst.": 3.2, "Ankara EAH": 4.1, "Dr. Sami Ulus": 5.5 },
  { name: "Bekleme Süresi", "Ankara Şehir Hst.": 15, "Ankara EAH": 22, "Dr. Sami Ulus": 28 },
];

const metrics = ["Puan Kaybı Haritası", "Başarı Oranı", "Gösterge Detay"];

const HospitalComparison = () => {
  const [selectedMetric, setSelectedMetric] = useState(metrics[0]);

  return (
    <div className="saglik-card p-5">
      <h3 className="saglik-section-title">Hastane Karşılaştırması</h3>
      <p className="saglik-section-desc">Birden fazla sağlık tesisini karşılaştırmalı olarak analiz edin</p>

      <div className="flex flex-col lg:flex-row gap-4 mb-6">
        <div className="flex-1">
          <label className="block text-sm font-medium mb-1.5">Karşılaştırılacak Hastaneler</label>
          <select multiple className="w-full rounded-md border border-input bg-card px-3 py-2 text-sm h-24 focus:outline-none focus:ring-2 focus:ring-ring">
            {allHospitals.map((h) => (
              <option key={h} value={h}>{h}</option>
            ))}
          </select>
          <span className="text-xs text-muted-foreground mt-1 block">En az 2 hastane seçiniz</span>
        </div>
        <div className="flex-1">
          <label className="block text-sm font-medium mb-1.5">Metrik</label>
          <select
            value={selectedMetric}
            onChange={(e) => setSelectedMetric(e.target.value)}
            className="w-full rounded-md border border-input bg-card px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring"
          >
            {metrics.map((m) => (
              <option key={m} value={m}>{m}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Insight bar */}
      <div className="flex items-center gap-4 p-3 rounded-lg bg-background border border-border mb-6">
        <span className="text-sm font-medium">3 hastane seçili</span>
        <span className="text-sm text-muted-foreground">·</span>
        <span className="text-sm text-muted-foreground">5 gösterge üzerinden karşılaştırma</span>
      </div>

      <ResponsiveContainer width="100%" height={320}>
        <BarChart data={comparisonData}>
          <CartesianGrid strokeDasharray="3 3" stroke="hsl(210, 18%, 88%)" />
          <XAxis dataKey="name" tick={{ fontSize: 12 }} />
          <YAxis tick={{ fontSize: 13 }} />
          <Tooltip />
          <Legend />
          <Bar dataKey="Ankara Şehir Hst." fill="#DC0D15" radius={[4, 4, 0, 0]} barSize={20} />
          <Bar dataKey="Ankara EAH" fill="#0095C6" radius={[4, 4, 0, 0]} barSize={20} />
          <Bar dataKey="Dr. Sami Ulus" fill="#55BAB7" radius={[4, 4, 0, 0]} barSize={20} />
        </BarChart>
      </ResponsiveContainer>

      <div className="flex items-center gap-6 mt-4 text-sm">
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-sm bg-primary" />
          <span>Seçili Hastane</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-sm bg-saglik-info" />
          <span>Karşılaştırma Hastaneleri</span>
        </div>
      </div>
    </div>
  );
};

export default HospitalComparison;
