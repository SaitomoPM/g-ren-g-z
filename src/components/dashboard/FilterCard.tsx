import { Star, HelpCircle, FileSpreadsheet, BarChart3, Sparkles } from "lucide-react";

const hospitals = [
  {
    group: "Genel Hastaneler",
    items: ["Ankara Şehir Hastanesi", "Ankara Eğitim ve Araştırma Hastanesi", "Dr. Sami Ulus Hastanesi"],
  },
  {
    group: "ADSM",
    items: ["Altındağ ADSM", "Çankaya ADSM", "Keçiören ADSM"],
  },
  {
    group: "ADSH",
    items: ["Ankara ADSH", "Gölbaşı ADSH"],
  },
];

const indicators = [
  "Acil Servis Bekleme Süresi",
  "Yatak Doluluk Oranı",
  "Ameliyat İptal Oranı",
  "Hasta Memnuniyeti",
  "Enfeksiyon Hızı",
  "Ortalama Yatış Süresi",
];

const FilterCard = () => {
  return (
    <div className="saglik-card p-4">
      <div className="flex flex-col lg:flex-row gap-4">
        {/* Hospital Selector */}
        <div className="flex-1">
          <label className="block text-sm font-medium text-foreground mb-1.5">
            Sağlık Tesisi Seçimi
          </label>
          <select className="w-full rounded-md border border-input bg-card px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring">
            {hospitals.map((group) => (
              <optgroup key={group.group} label={group.group}>
                {group.items.map((item) => (
                  <option key={item} value={item}>{item}</option>
                ))}
              </optgroup>
            ))}
          </select>
        </div>

        {/* Indicator Selector */}
        <div className="flex-1">
          <label className="block text-sm font-medium text-foreground mb-1.5">
            Gösterge Seçimi
          </label>
          <div className="flex gap-2">
            <select className="flex-1 rounded-md border border-input bg-card px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring">
              {indicators.map((ind) => (
                <option key={ind} value={ind}>{ind}</option>
              ))}
            </select>
            <div className="flex items-center gap-1">
              <button className="saglik-btn-ghost p-2" title="Favorilere ekle" aria-label="Favorilere ekle">
                <Star className="w-4 h-4" />
              </button>
              <button className="saglik-btn-ghost p-2" title="Bilgi" aria-label="Bilgi">
                <HelpCircle className="w-4 h-4" />
              </button>
              <button className="saglik-btn-ghost p-2" title="Excel dışa aktar" aria-label="Excel dışa aktar">
                <FileSpreadsheet className="w-4 h-4" />
              </button>
              <button className="saglik-btn-ghost p-2" title="SWOT raporu" aria-label="SWOT raporu">
                <BarChart3 className="w-4 h-4" />
              </button>
              <button className="saglik-btn-ghost p-2 text-purple-600" title="Yapay zeka önerileri" aria-label="Yapay zeka önerileri">
                <Sparkles className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FilterCard;
