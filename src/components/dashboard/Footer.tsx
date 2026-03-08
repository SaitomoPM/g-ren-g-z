import { ArrowUp, HelpCircle } from "lucide-react";

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <footer className="bg-card border-t border-border mt-8">
      <div className="saglik-container py-4 flex items-center justify-between text-sm text-muted-foreground">
        <div className="flex items-center gap-4">
          <span>Son veri güncellemesi: 07.03.2026 14:30</span>
          <span>·</span>
          <span>2026 Q1 Dönemi · 42 Gösterge</span>
        </div>
        <div className="flex items-center gap-4">
          <button className="flex items-center gap-1 hover:text-foreground transition-colors">
            <HelpCircle className="w-4 h-4" />
            Yardım
          </button>
          <button
            onClick={scrollToTop}
            className="flex items-center justify-center w-8 h-8 rounded-md bg-muted hover:bg-border transition-colors"
            aria-label="Yukarı çık"
          >
            <ArrowUp className="w-4 h-4" />
          </button>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
