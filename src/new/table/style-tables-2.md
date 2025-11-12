<style>
.table-wrapper {
  width: 100%;
  overflow-x: auto;
  margin: 20px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed; /* Equal column widths */
  font-family: 'Segoe UI', sans-serif;
  font-size: 15px;
}

th, td {
  padding: 12px;
  text-align: left;
  border: 1px solid #ccc;
  white-space: normal;
  word-wrap: break-word;
}

th {
  background-color: #fdf3e7; /* Warm beige header */
  color: #1565c0; /* Blue accent for text */
  font-weight: 600;
}

tr:nth-child(even) td {
  background-color: #f9fcff; /* Light blue tint for alternating rows */
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  table { background-color: #1a1a1a; color: #e0e0e0; }
  th { background-color: #333; color: #cce4ff; }
  td { border-color: #444; }
  tr:nth-child(even) td { background-color: #222; }
}
</style>
