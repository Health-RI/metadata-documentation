
<style>
  :root {
    --table-font: 'Segoe UI', sans-serif;
    --table-font-size: 15px;
    --table-border: 1px solid #d0d0d0;
    --table-header-bg: #e8f0fe;
    --table-header-color: #2d3e50;
    --table-row-even: #f5faff;
    --table-row-odd: #ffffff;
    --table-padding: 14px;
    --table-col-width: 200px;
  }

  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    font-family: var(--table-font);
    font-size: var(--table-font-size);
  }

  th, td {
    padding: var(--table-padding);
    text-align: left;
    border: var(--table-border);
    word-wrap: break-word;
    overflow-wrap: break-word;
    hyphens: auto;
    width: var(--table-col-width);
  }

  th {
    background-color: var(--table-header-bg);
    color: var(--table-header-color);
    font-weight: 600;
  }

  tr:nth-child(even) {
    background-color: var(--table-row-even);
  }

  tr:nth-child(odd) {
    background-color: var(--table-row-odd);
  }

  /* Dark mode overrides */
  @media (prefers-color-scheme: dark) {
    :root {
      --table-border: 1px solid #444;
      --table-header-bg: #2a2a2a;
      --table-header-color: #f0f0f0;
      --table-row-even: #1e1e1e;
      --table-row-odd: #121212;
    }

    body {
      background-color: #000;
      color: #ccc;
    }
  }
</style>
