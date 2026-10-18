const API_URL = "https://academia-sistem.onrender.com";

async function requisicao(caminho, opcoes = {}) {
    const configuracao = {
        ...opcoes,
        headers: {
            ...(opcoes.body ? { "Content-Type": "application/json" } : {}),
            ...opcoes.headers
        }
    };

    const resposta = await fetch(`${API_URL}${caminho}`, configuracao);

    if (resposta.status === 204) {
        return null;
    }

    const texto = await resposta.text();

    let dados = null;

    if (texto) {
        try {
            dados = JSON.parse(texto);
        } catch {
            dados = texto;
        }
    }

    if (!resposta.ok) {
        let mensagem = `Erro HTTP ${resposta.status}`;

        if (dados && typeof dados === "object") {
            if (Array.isArray(dados.detail)) {
                mensagem = dados.detail
                    .map(erro => erro.msg || JSON.stringify(erro))
                    .join("; ");
            } else if (typeof dados.detail === "string") {
                mensagem = dados.detail;
            } else if (typeof dados.message === "string") {
                mensagem = dados.message;
            }
        } else if (typeof dados === "string" && dados) {
            mensagem = dados;
        }

        throw new Error(mensagem);
    }

    return dados;
}

function $(seletor) {
    return document.querySelector(seletor);
}

function escaparHTML(valor) {
    return String(valor ?? "").replace(/[&<>"']/g, caractere => {
        const caracteres = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        };

        return caracteres[caractere];
    });
}

function mostrarMensagem(texto, tipo = "sucesso") {
    const elemento = $("#mensagem");

    elemento.textContent = texto;
    elemento.className = `mensagem ${tipo}`;
    elemento.hidden = false;
}

function mostrarErro(erro) {
    console.error(erro);
    mostrarMensagem(erro.message || "Ocorreu um erro inesperado.", "erro");
}

function formatarPlano(plano) {
    const planos = {
        basico: "Básico",
        intermediario: "Intermediário",
        pro: "Pro"
    };

    return planos[plano] || plano;
}

function formatarDia(dia) {
    const dias = {
        segunda: "Segunda-feira",
        terca: "Terça-feira",
        quarta: "Quarta-feira",
        quinta: "Quinta-feira",
        sexta: "Sexta-feira",
        sabado: "Sábado",
        domingo: "Domingo"
    };

    return dias[dia] || dia;
}

function mostrarSecao(nome) {
    const secoes = document.querySelectorAll(".secao");
    const botoes = document.querySelectorAll(".menu-item");

    secoes.forEach(secao => {
        secao.classList.toggle("ativa", secao.id === `secao-${nome}`);
    });

    botoes.forEach(botao => {
        botao.classList.toggle("ativo", botao.dataset.secao === nome);
    });

    const titulos = {
        alunos: "Alunos",
        treinos: "Treinos",
        exercicios: "Exercícios"
    };

    $("#titulo-pagina").textContent = titulos[nome] || "Sistema";

    const mensagem = $("#mensagem");
    mensagem.hidden = true;
}

document.querySelectorAll(".menu-item").forEach(botao => {
    botao.addEventListener("click", () => {
        mostrarSecao(botao.dataset.secao);
    });
});