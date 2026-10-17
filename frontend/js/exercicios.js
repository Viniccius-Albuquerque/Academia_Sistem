$("#form-exercicio").addEventListener("submit", async evento => {
    evento.preventDefault();

    const exercicio = {
        nome: $("#exercicio-nome").value.trim(),
        series: Number($("#exercicio-series").value),
        repeticoes: Number($("#exercicio-repeticoes").value),
        id_treino: Number($("#exercicio-treino").value)
    };

    try {
        await requisicao("/exercicio/", {
            method: "POST",
            body: JSON.stringify(exercicio)
        });

        $("#form-exercicio").reset();

        mostrarMensagem("Exercício cadastrado com sucesso!");

        if (ultimoTreinoConsultado === exercicio.id_treino) {
            await carregarExercicios(exercicio.id_treino);
        }

    } catch (erro) {
        mostrarErro(erro);
    }
});

let ultimoTreinoConsultado = null;

async function carregarExercicios(idTreino) {
    const tabela = $("#lista-exercicios");

    ultimoTreinoConsultado = idTreino;

    tabela.innerHTML = `
        <tr>
            <td colspan="6" class="tabela-vazia">Carregando exercícios...</td>
        </tr>
    `;

    try {
        const exercicios = await requisicao(`/exercicio/${idTreino}`);

        tabela.innerHTML = "";

        if (exercicios.length === 0) {
            tabela.innerHTML = `
                <tr>
                    <td colspan="6" class="tabela-vazia">
                        Este treino ainda não possui exercícios.
                    </td>
                </tr>
            `;
            return;
        }

        exercicios.forEach(exercicio => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${escaparHTML(exercicio.id)}</td>
                <td>${escaparHTML(exercicio.nome)}</td>
                <td>${escaparHTML(exercicio.series)}</td>
                <td>${escaparHTML(exercicio.repeticoes)}</td>
                <td>${escaparHTML(exercicio.id_treino)}</td>
                <td>
                    <div class="acoes-tabela">
                        <button
                            type="button"
                            class="botao botao-secundario botao-pequeno"
                            data-acao-exercicio="editar"
                            data-id="${escaparHTML(exercicio.id)}"
                            data-nome="${escaparHTML(exercicio.nome)}"
                            data-series="${escaparHTML(exercicio.series)}"
                            data-repeticoes="${escaparHTML(exercicio.repeticoes)}"
                            data-treino="${escaparHTML(exercicio.id_treino)}"
                        >
                            Editar
                        </button>

                        <button
                            type="button"
                            class="botao botao-perigo botao-pequeno"
                            data-acao-exercicio="remover"
                            data-id="${escaparHTML(exercicio.id)}"
                        >
                            Excluir
                        </button>
                    </div>
                </td>
            `;

            tabela.appendChild(linha);
        });

    } catch (erro) {
        tabela.innerHTML = `
            <tr>
                <td colspan="6" class="tabela-vazia">
                    Não foi possível carregar os exercícios.
                </td>
            </tr>
        `;

        mostrarErro(erro);
    }
}

$("#buscar-exercicios").addEventListener("submit", async evento => {
    evento.preventDefault();

    const idTreino = Number($("#buscar-exercicio-treino").value);

    await carregarExercicios(idTreino);
});

$("#lista-exercicios").addEventListener("click", async evento => {
    const botao = evento.target.closest("button[data-acao-exercicio]");

    if (!botao) {
        return;
    }

    const id = botao.dataset.id;
    const acao = botao.dataset.acaoExercicio;

    try {
        if (acao === "editar") {
            const nomeAtual = botao.dataset.nome;
            const seriesAtual = botao.dataset.series;
            const repeticoesAtual = botao.dataset.repeticoes;

            const novoNome = prompt("Nome do exercício:", nomeAtual);

            if (novoNome === null) {
                return;
            }

            if (!novoNome.trim()) {
                throw new Error("O nome do exercício não pode ficar vazio.");
            }

            const novasSeries = prompt("Quantidade de séries:", seriesAtual);

            if (novasSeries === null) {
                return;
            }

            const series = Number(novasSeries);

            if (!Number.isInteger(series) || series <= 0) {
                throw new Error("As séries devem ser um número inteiro maior que zero.");
            }

            const novasRepeticoes = prompt(
                "Quantidade de repetições:",
                repeticoesAtual
            );

            if (novasRepeticoes === null) {
                return;
            }

            const repeticoes = Number(novasRepeticoes);

            if (!Number.isInteger(repeticoes) || repeticoes <= 0) {
                throw new Error("As repetições devem ser um número inteiro maior que zero.");
            }

            await requisicao(`/exercicio/atualizar/${id}`, {
                method: "PUT",
                body: JSON.stringify({
                    nome: novoNome.trim(),
                    series,
                    repeticoes
                })
            });

            mostrarMensagem("Exercício atualizado com sucesso!");

            if (ultimoTreinoConsultado !== null) {
                await carregarExercicios(ultimoTreinoConsultado);
            }

        } else if (acao === "remover") {
            const confirmacao = confirm(
                "Deseja realmente excluir este exercício?"
            );

            if (!confirmacao) {
                return;
            }

            await requisicao(`/exercicio/delete/${id}`, {
                method: "DELETE"
            });

            mostrarMensagem("Exercício excluído com sucesso!");

            if (ultimoTreinoConsultado !== null) {
                await carregarExercicios(ultimoTreinoConsultado);
            }
        }

    } catch (erro) {
        mostrarErro(erro);
    }
});