document.addEventListener("DOMContentLoaded", function () {
    const toggles = document.querySelectorAll('.col-toggle');

    function aplicarVisibilidade(colName, isChecked) {
        // Tabela Principal (mostra se marcado, esconde se desmarcado)
        document.querySelectorAll(`.col-main.col-${colName}`).forEach(el => {
            el.style.display = isChecked ? '' : 'none';
        });

        // Tabela de Detalhes (esconde se marcado, mostra se desmarcado)
        document.querySelectorAll(`.col-detail.col-${colName}`).forEach(el => {
            el.style.display = isChecked ? 'none' : 'table-cell'; // table-cell mantém o grid da tabela alinhado
        });
    }

    toggles.forEach(toggle => {
        const colName = toggle.getAttribute('data-col');

        // Carrega estado salvo
        const savedState = localStorage.getItem(`pref_col_${colName}`);
        if (savedState !== null) {
            toggle.checked = savedState === 'true';
        }

        // Aplica estado inicial
        aplicarVisibilidade(colName, toggle.checked);

        // Escuta mudanças
        toggle.addEventListener('change', function () {
            aplicarVisibilidade(colName, this.checked);
            localStorage.setItem(`pref_col_${colName}`, this.checked);
        });
    });
});