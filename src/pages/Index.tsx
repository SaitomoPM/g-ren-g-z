import { useState } from "react";
import Header from "@/components/dashboard/Header";
import FilterCard from "@/components/dashboard/FilterCard";
import ScoreCards from "@/components/dashboard/ScoreCards";
import InsightCards from "@/components/dashboard/InsightCards";
import PeriodSelector from "@/components/dashboard/PeriodSelector";
import ChartsSection from "@/components/dashboard/ChartsSection";
import HospitalComparison from "@/components/dashboard/HospitalComparison";
import Footer from "@/components/dashboard/Footer";

const Index = () => {
  const [activeTab, setActiveTab] = useState<"goren" | "rapor">("goren");
  const [period, setPeriod] = useState("6 Ay");
  const [yoy, setYoy] = useState(false);

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <main className="saglik-container py-6 space-y-6">
        {/* Filter Card */}
        <FilterCard />

        {/* Tab Switcher */}
        <div className="flex border-b border-border">
          <button
            onClick={() => setActiveTab("goren")}
            className={`px-6 py-2.5 text-sm font-semibold border-b-2 transition-colors ${
              activeTab === "goren"
                ? "border-primary text-primary"
                : "border-transparent text-muted-foreground hover:text-foreground"
            }`}
          >
            GÖREN
          </button>
          <button
            onClick={() => setActiveTab("rapor")}
            className={`px-6 py-2.5 text-sm font-semibold border-b-2 transition-colors ${
              activeTab === "rapor"
                ? "border-primary text-primary"
                : "border-transparent text-muted-foreground hover:text-foreground"
            }`}
          >
            Rapor Kartı
          </button>
        </div>

        {activeTab === "goren" ? (
          <div className="space-y-6">
            {/* Scorecards */}
            <ScoreCards />

            {/* Period Comparison */}
            <div className="saglik-card p-5">
              <h3 className="saglik-section-title">Dönem Karşılaştırması</h3>
              <p className="saglik-section-desc">Önceki dönemle değişim analizi</p>
              <select className="rounded-md border border-input bg-card px-3 py-2 text-sm mb-4 focus:outline-none focus:ring-2 focus:ring-ring">
                <option>2025 Q4 ile karşılaştır</option>
                <option>2025 Q3 ile karşılaştır</option>
                <option>2024 Q1 ile karşılaştır (YoY)</option>
              </select>
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
                {[
                  { label: "Toplam GP", current: "87.4", prev: "85.3", up: true },
                  { label: "Başarı Oranı", current: "%78.5", prev: "%74.3", up: true },
                  { label: "GD Ortalaması", current: "3.28", prev: "3.43", up: false },
                  { label: "Gösterge Sayısı", current: "42", prev: "42", up: null },
                ].map((d) => (
                  <div key={d.label} className="p-3 rounded-lg bg-background border border-border text-center">
                    <div className="text-xs text-muted-foreground mb-1">{d.label}</div>
                    <div className="text-lg font-bold">{d.current}</div>
                    <div className={`text-xs mt-0.5 ${d.up === true ? "text-saglik-success" : d.up === false ? "text-saglik-warning" : "text-muted-foreground"}`}>
                      {d.up === true ? "▲" : d.up === false ? "▼" : "—"} {d.prev}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Insight Cards */}
            <InsightCards />

            {/* Period Selector */}
            <PeriodSelector selected={period} onSelect={setPeriod} yoyEnabled={yoy} onToggleYoy={() => setYoy(!yoy)} />

            {/* Charts */}
            <ChartsSection />

            {/* Hospital Comparison */}
            <HospitalComparison />
          </div>
        ) : (
          <div className="saglik-card p-8 text-center">
            <h3 className="saglik-section-title">Rapor Kartı</h3>
            <p className="text-muted-foreground">Rapor kartı içeriği burada gösterilecektir.</p>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

export default Index;
