const PeriodSelector = ({
  selected,
  onSelect,
  yoyEnabled,
  onToggleYoy,
}: {
  selected: string;
  onSelect: (val: string) => void;
  yoyEnabled: boolean;
  onToggleYoy: () => void;
}) => {
  const periods = ["6 Ay", "12 Ay", "Tümü"];

  return (
    <div className="flex items-center gap-4 flex-wrap">
      <div className="flex items-center bg-muted rounded-lg p-1">
        {periods.map((p) => (
          <button
            key={p}
            onClick={() => onSelect(p)}
            className={`px-4 py-1.5 text-sm rounded-md font-medium transition-colors ${
              selected === p
                ? "bg-card text-foreground shadow-sm"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            {p}
          </button>
        ))}
      </div>
      <label className="flex items-center gap-2 text-sm cursor-pointer">
        <input
          type="checkbox"
          checked={yoyEnabled}
          onChange={onToggleYoy}
          className="w-4 h-4 rounded border-input text-primary focus:ring-ring"
        />
        Önceki Yıl (YoY)
      </label>
    </div>
  );
};

export default PeriodSelector;
