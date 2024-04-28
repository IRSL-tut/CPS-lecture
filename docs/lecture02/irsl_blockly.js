Blockly.Blocks['getkey'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("getKey");
        this.appendEndRowInput()
            .appendField("async")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "async");
        this.setOutput(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    },
};
Blockly.Blocks['getButton'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("getButton");
        this.appendEndRowInput()
            .appendField("async")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "async");
        this.setOutput(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    },
};
Blockly.Blocks['start_from'] = {
    init: function() {
        this.appendValueInput("intext")
            .setCheck(null)
            .appendField("startFrom");
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['pass'] = {
    init: function() {
        this.appendValueInput("invalue")
            .setCheck(null)
            .appendField("pass");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['write_string'] = {
    init: function() {
        this.appendValueInput("intext")
            .setCheck(null)
            .appendField("write:String");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['write_newline'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("write:Newline");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['write_clear'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("write:Clear");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['end_with'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("endWith");
        this.setPreviousStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['text_to_logic'] = {
    init: function() {
        this.appendValueInput("intext")
            .setCheck("String")
            .appendField("text_to_logic");
        this.setOutput(true, "Boolean");
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['text_to_number'] = {
    init: function() {
        this.appendValueInput("intext")
            .setCheck("String")
            .appendField("text_to_number");
        this.setOutput(true, "Number");
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['high_light'] = {
    init: function() {
        this.appendEndRowInput()
            .appendField("highlight")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "hl");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['async_blocks'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("async_blocks");
        this.appendStatementInput("async_f")
            .setCheck(null);
        this.setStyle('robot_blocks')
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
// code generations
javascript.javascriptGenerator.forBlock['getkey'] = function(block, generator) {
    var checkbox_async = block.getFieldValue('async') === 'TRUE';
    var code = 'await myGetKey()';
    // await myGetKey
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, javascript.Order.NONE];
};
javascript.javascriptGenerator.forBlock['getButton'] = function(block, generator) {
    var checkbox_async = block.getFieldValue('async') === 'TRUE';
    var code = 'await getButton()';
    // await myGetKey
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, javascript.Order.NONE];
};
javascript.javascriptGenerator.forBlock['start_from'] = function(block, generator) {
    var value_intext = generator.valueToCode(block, 'intext', javascript.Order.ATOMIC);
    var code = 'start_from(' + value_input + ');\n';
    return code;
};
javascript.javascriptGenerator.forBlock['pass'] = function(block, generator) {
    var value_invalue = generator.valueToCode(block, 'invalue', javascript.Order.ATOMIC);
    var code = value_invalue + ';\n';
    return code;
};
javascript.javascriptGenerator.forBlock['end_with'] = function(block, generator) {
    var code = 'end_with();\n';
    return code;
};
javascript.javascriptGenerator.forBlock['write_string'] = function(block, generator) {
    var value_intext = generator.valueToCode(block, 'intext', javascript.Order.ATOMIC);
    var code = 'write_string(' + value_intext + ');\n';
    return code;
};
javascript.javascriptGenerator.forBlock['write_newline'] = function(block, generator) {
    var code = 'write_string("\\n");\n';
    return code;
};
javascript.javascriptGenerator.forBlock['write_clear'] = function(block, generator) {
    var code = 'write_clear();\n';
    return code;
};
javascript.javascriptGenerator.forBlock['pass'] = function(block, generator) {
    var value_invalue = generator.valueToCode(block, 'invalue', javascript.Order.ATOMIC);
    var code = value_invalue + ';\n';
    return code;
};
javascript.javascriptGenerator.forBlock['text_to_logic'] = function(block, generator) {
    var value_intext = generator.valueToCode(block, 'intext', javascript.Order.ATOMIC);
    var code = 'f_text_to_logic(' + value_intext + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, javascript.Order.NONE];
};
javascript.javascriptGenerator.forBlock['text_to_number'] = function(block, generator) {
    var value_intext = generator.valueToCode(block, 'intext', javascript.Order.ATOMIC);
    var code = 'f_text_to_number(' + value_intext + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, javascript.Order.NONE];
};
javascript.javascriptGenerator.forBlock['high_light'] = function(block, generator) {
    var checkbox_hl = block.getFieldValue('hl') === 'TRUE';
    var code = 'set_enable_highlight(' + checkbox_hl + ');\n';
    return code;
};
javascript.javascriptGenerator.forBlock['async_blocks'] = function(block, generator) {
    var statements_async_f = generator.statementToCode(block, 'async_f');
    var code = '(async () => {\n' + statements_async_f + '\n})();\n';
    return code;
};
