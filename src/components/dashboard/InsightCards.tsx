import { ArrowUp, ArrowDown, AlertTriangle } from "lucide-react";

const monthlyChanges = [
  { name: "Hasta Memnuniyeti", delta: "+5.2", up: true },
  { name: "Yatak Doluluk Oranı", delta: "+3.1", up: true },
  { name: "Ameliyat İptal Oranı", delta: "-2.8", up: false },
  { name: "Enfeksiyon Hızı", delta: "-1.5", up: false },
];

const priorities = [
  { name: "Acil Servis Bekleme Süresi", gpLoss: "4.2 GP", rank: 1 },
  { name: "Ameliyat İptal Oranı", gpLoss: "3.1 GP", rank: 2 },
  { name: "Enfeksiyon Hızı", gpLoss: "2.7 GP", rank: 3 },
  { name: "Lab Sonuç Süresi", gpLoss: "1.9 GP", rank: 4 },
];

const InsightCards = () => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
      {/* Monthly Changes */}
      <div className="saglik-card p-5 border-t-4 border-t-saglik-warning">
        <h3 className="saglik-section-title flex items-center gap-2">
          <ArrowUp className="w-5 h-5 text-saglik-warning" />
          Aylık Değişim
        </h3>
        <p className="saglik-section-desc">Son aya göre iyileşen ve gerileyen göstergeler</p>
        <ul className="space-y-2">
          {monthlyChanges.map((item) => (
            <li key={item.name} className="flex items-center justify-between py-1.5 border-b border-border last:border-0">
              <span className="text-sm">{item.name}</span>
              <span className={`flex items-center gap-1 text-sm font-medium ${item.up ? "text-saglik-success" : "text-saglik-warning"}`}>
                {item.up ? <ArrowUp className="w-3.5 h-3.5" /> : <ArrowDown className="w-3.5 h-3.5" />}
                {item.delta}
              </span>
            </li>
          ))}
        </ul>
      </div>

      {/* Smart Priority */}
      <div className="saglik-card p-5 border-t-4 border-t-saglik-threat">
        <h3 className="saglik-section-title flex items-center gap-2">
          <AlertTriangle className="w-5 h-5 text-saglik-threat" />
          Akıllı Öncelik
        </h3>
        <p className="saglik-section-desc">GP kaybına göre sıralanmış düşük performanslı göstergeler</p>
        <ul className="space-y-2">
          {priorities.map((item) => (
            <li key={item.name} className="flex items-center justify-between py-1.5 border-b border-border last:border-0">
              <span className="text-sm">
                <span className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-saglik-threat text-primary-foreground text-xs font-bold mr-2">
                  {item.rank}
                </span>
                {item.name}
              </span>
              <span className="text-sm font-medium text-saglik-warning">-{item.gpLoss}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default InsightCards;
