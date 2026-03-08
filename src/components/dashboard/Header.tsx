import { Bell, LogOut, Settings, Upload, RefreshCw, Printer, Key, Shield, FileText } from "lucide-react";
import mohLogo from "@/assets/moh-logo.png";

const Header = () => {
  return (
    <header className="sticky top-0 z-50">
      {/* Government Strip */}
      <div className="saglik-gov-strip flex items-center justify-between px-4 text-primary-foreground text-xs">
        <span className="font-medium">T.C. Sağlık Bakanlığı · Ankara İl Sağlık Müdürlüğü</span>
        <div className="flex items-center gap-3">
          <button className="relative" aria-label="Bildirimler">
            <Bell className="w-4 h-4" />
            <span className="absolute -top-1 -right-1 w-3.5 h-3.5 bg-card text-primary rounded-full text-[9px] font-bold flex items-center justify-center">3</span>
          </button>
          <span>kullanici@saglik.gov.tr</span>
          <button className="flex items-center gap-1 hover:opacity-80 transition-opacity">
            <LogOut className="w-3.5 h-3.5" />
            Çıkış
          </button>
        </div>
      </div>

      {/* Brand Bar */}
      <div className="bg-card border-b border-border px-4 py-2">
        <div className="saglik-container flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img src={mohLogo} alt="T.C. Sağlık Bakanlığı logosu" className="w-11 h-11 object-contain" />
            <div>
              <div className="text-sm text-muted-foreground font-medium">Ankara İl Sağlık Müdürlüğü</div>
              <div className="text-base font-semibold">
                <span className="text-primary font-bold">GÖREN</span>{" "}
                Performans Takip Sistemi
              </div>
            </div>
          </div>
          <nav className="flex items-center gap-1">
            {[
              { icon: Shield, label: "Admin Panel" },
              { icon: Settings, label: "Ayarlar" },
              { icon: Upload, label: "Veri Yükle" },
              { icon: FileText, label: "Yönetici Özeti" },
              { icon: RefreshCw, label: "Yenile" },
              { icon: Printer, label: "Yazdır" },
              { icon: Key, label: "Şifre Değiştir" },
            ].map(({ icon: Icon, label }) => (
              <button key={label} className="saglik-btn-ghost text-xs">
                <Icon className="w-4 h-4" />
                <span className="hidden xl:inline">{label}</span>
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Context Bar */}
      <div className="bg-muted border-b border-border px-4 py-1.5 text-sm">
        <div className="saglik-container flex items-center justify-between">
          <span className="font-medium">Ankara Şehir Hastanesi</span>
          <span className="text-muted-foreground">Son güncelleme: 07.03.2026 14:30</span>
        </div>
      </div>
    </header>
  );
};

export default Header;
