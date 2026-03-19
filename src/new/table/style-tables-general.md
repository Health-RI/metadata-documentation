<style>
/* ===== Global table style (unchanged) ===== */
table {
  border-collapse: collapse;
  font-family: sans-serif;
  font-size: 11px;
  line-height: 1.2;
}

th, td {
  border: 1px solid #ccc;
  padding: 2px 4px;
  text-align: left;
  vertical-align: top;
}

th {
  background: #d9edf7;
  font-weight: bold;
}

tr:nth-child(even) {
  background: #f9f9f9;
}

tr:hover {
  background: #e6f2ff;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  table {
    background-color: #111;
    color: #eee;
  }
  th {
    background-color: #004466;
    color: #fff;
  }
  td {
    border: 1px solid #444;
  }
  tr:nth-child(even) {
    background-color: #1a1a1a;
  }
  tr:hover {
    background-color: #333366;
  }
}

/* ===== OVERRIDE ONLY THIS TABLE ===== */
table.no-style,
table.no-style th,
table.no-style td {
  border: none !important;
  background: none !important;
  font-size: 12.5px !important;    /* larger text */
  line-height: 1.4 !important;   /* better readability */
  margin-bottom: 1.5em;          /* space after table */
}

table.no-style th,
table.no-style td {
  padding: 0.2em 0.8em 0.4em 0 !important;  /* extra padding for spacing */
}

/* Top line for header */
table.no-style thead th {
  border-bottom: 1px solid #aaaaaa00 !important;
}

/* Bottom line under last row */
table.no-style tr:last-child td {
  border-bottom: 1px solid #aaaaaa00 !important;
}
</style>