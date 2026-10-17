async function carregarAlunos() {
    const tabela = $("#lista-alunos");

    tabela.innerHTML = `
        <tr>
            <td colspan="6" class="tabela-vazia">Carregando alunos...</td>
        </tr>
    `;

    try {
        const alunos = await requisicao("/alunos/");

        tabela.innerHTML = "";

        $("#total-alunos").textContent = alunos.length;

        const ativos = alunos.filter(aluno =>
            String(aluno.estado).toLowerCase() === "ativo"
        ).length;

        $("#ativos-alunos").textContent = ativos;
        $("#inativos-alunos").textContent = alunos.length - ativos;

        if (alunos.length === 0) {
            tabela.innerHTML = `
                <tr>
                    <td colspan="6" class="tabela-vazia">
                        Nenhum aluno cadastrado.
                    </td>
                </tr>
            `;
            return;
        }

        alunos.forEach(aluno => {
            const ativo = String(aluno.estado).toLowerCase() === "ativo";

            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${escaparHTML(aluno.id)}</td>
                <td>${escaparHTML(aluno.nome)}</td>
                <td>${escaparHTML(aluno.idade)}</td>
                <td>${escaparHTML(formatarPlano(aluno.plano))}</td>
                <td>
                    <span class="estado ${ativo ? "estado-ativo" : "estado-inativo"}">
                        ${escaparHTML(aluno.estado)}
                    </span>
                </td>
                <td>
                    <div class="acoes-tabela">
                        <button
                            type="button"
                            class="botao botao-secundario botao-pequeno"
                            data-acao-aluno="editar"
                            data-id="${escaparHTML(aluno.id)}"
                            data-nome="${escaparHTML(aluno.nome)}"
                            data-idade="${escaparHTML(aluno.idade)}"
                            data-plano="${escaparHTML(aluno.plano)}"
                        >
                            Editar
                        </button>

                        <button
                            type="button"
                            class="botao botao-secundario botao-pequeno"
                            data-acao-aluno="${ativo ? "desativar" : "ativar"}"
                            data-id="${escaparHTML(aluno.id)}"
                        >
                            ${ativo ? "Desativar" : "Ativar"}
                        </button>

                        <button
                            type="button"
                            class="botao botao-perigo botao-pequeno"
                            data-acao-aluno="remover"
                            data-id="${escaparHTML(aluno.id)}"
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
                    Não foi possível carregar os alunos.
                </td>
            </tr>
        `;

        mostrarErro(erro);
    }
}

$("#form-aluno").addEventListener("submit", async evento => {
    evento.preventDefault();

    const aluno = {
        nome: $("#aluno-nome").value.trim(),
        idade: Number($("#aluno-idade").value),
        plano: $("#aluno-plano").value
    };

    try {
        await requisicao("/alunos/", {
            method: "POST",
            body: JSON.stringify(aluno)
        });

        $("#form-aluno").reset();

        mostrarMensagem("Aluno cadastrado com sucesso!");
        await carregarAlunos();

    } catch (erro) {
        mostrarErro(erro);
    }
});

$("#atualizar-lista-alunos").addEventListener("click", carregarAlunos);

$("#lista-alunos").addEventListener("click", async evento => {
    const botao = evento.target.closest("button[data-acao-aluno]");

    if (!botao) {
        return;
    }

    const id = botao.dataset.id;
    const acao = botao.dataset.acaoAluno;

    try {
        if (acao === "editar") {
            const idadeAtual = botao.dataset.idade;
            const planoAtual = botao.dataset.plano;

            const novaIdade = prompt(
                "Informe a nova idade:",
                idadeAtual
            );

            if (novaIdade === null) {
                return;
            }

            const idade = Number(novaIdade);

            if (!Number.isInteger(idade) || idade <= 0) {
                throw new Error("A idade precisa ser um número inteiro maior que zero.");
            }

            const novoPlano = prompt(
                "Informe o novo plano: basico, intermediario ou pro",
                planoAtual
            );

            if (novoPlano === null) {
                return;
            }

            const plano = novoPlano.trim().toLowerCase();

            if (!["basico", "intermediario", "pro"].includes(plano)) {
                throw new Error("Plano inválido. Use basico, intermediario ou pro.");
            }

            await requisicao(`/alunos/${id}`, {
                method: "PATCH",
                body: JSON.stringify({
                    idade,
                    plano
                })
            });

            mostrarMensagem("Aluno atualizado com sucesso!");

        } else if (acao === "ativar" || acao === "desativar") {
            const confirmacao = confirm(
                `Deseja realmente ${acao} este aluno?`
            );

            if (!confirmacao) {
                return;
            }

            const caminho = acao === "ativar"
                ? `/alunos/ativar/${id}`
                : `/alunos/desativar/${id}`;

            await requisicao(caminho, {
                method: "PATCH"
            });

            mostrarMensagem(
                acao === "ativar"
                    ? "Aluno ativado com sucesso!"
                    : "Aluno desativado com sucesso!"
            );

        } else if (acao === "remover") {
            const confirmacao = confirm(
                "Deseja realmente excluir este aluno? Essa ação pode ser irreversível."
            );

            if (!confirmacao) {
                return;
            }

            await requisicao(`/alunos/${id}`, {
                method: "DELETE"
            });

            mostrarMensagem("Aluno excluído com sucesso!");
        }

        await carregarAlunos();

    } catch (erro) {
        mostrarErro(erro);
    }
});

document.addEventListener("DOMContentLoaded", carregarAlunos);


/* ===================================== */
/* BUSCAR ALUNO POR ID                   */
/* ===================================== */

$("#buscar-aluno-id").addEventListener("submit", async evento => {
    evento.preventDefault();

    const id = Number($("#consulta-aluno-id").value);
    const tabela = $("#resultado-aluno-id");

    tabela.innerHTML = `
        <tr>
            <td colspan="5" class="tabela-vazia">
                Buscando aluno...
            </td>
        </tr>
    `;

    try {
        const aluno = await requisicao(`/alunos/id/${id}`);

        tabela.innerHTML = `
            <tr>
                <td>${escaparHTML(aluno.id)}</td>
                <td>${escaparHTML(aluno.nome)}</td>
                <td>${escaparHTML(aluno.idade)}</td>
                <td>${escaparHTML(formatarPlano(aluno.plano))}</td>
                <td>${escaparHTML(aluno.estado)}</td>
            </tr>
        `;

        mostrarMensagem(`Aluno de ID ${id} encontrado.`);

    } catch (erro) {
        tabela.innerHTML = `
            <tr>
                <td colspan="5" class="tabela-vazia">
                    Nenhum aluno encontrado com esse ID.
                </td>
            </tr>
        `;

        mostrarErro(erro);
    }
});

$("#buscar-alunos-plano").addEventListener("submit", async evento => {
    evento.preventDefault();

    const plano = $("#consulta-aluno-plano").value;
    const tabela = $("#resultado-alunos-plano");

    tabela.innerHTML = `
        <tr>
            <td colspan="5" class="tabela-vazia">
                Buscando alunos...
            </td>
        </tr>
    `;

    try {
        const alunos = await requisicao(
            `/alunos/plano/${encodeURIComponent(plano)}`
        );

        tabela.innerHTML = "";

        if (!Array.isArray(alunos) || alunos.length === 0) {
            tabela.innerHTML = `
                <tr>
                    <td colspan="5" class="tabela-vazia">
                        Nenhum aluno encontrado nesse plano.
                    </td>
                </tr>
            `;

            mostrarMensagem(
                `Nenhum aluno encontrado no plano ${formatarPlano(plano)}.`
            );

            return;
        }

        alunos.forEach(aluno => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${escaparHTML(aluno.id)}</td>
                <td>${escaparHTML(aluno.nome)}</td>
                <td>${escaparHTML(aluno.idade)}</td>
                <td>${escaparHTML(formatarPlano(aluno.plano))}</td>
                <td>${escaparHTML(aluno.estado)}</td>
            `;

            tabela.appendChild(linha);
        });

        mostrarMensagem(
            `${alunos.length} aluno(s) encontrado(s) no plano ${formatarPlano(plano)}.`
        );

    } catch (erro) {
        tabela.innerHTML = `
            <tr>
                <td colspan="5" class="tabela-vazia">
                    Não foi possível buscar alunos por plano.
                </td>
            </tr>
        `;

        mostrarErro(erro);
    }
});