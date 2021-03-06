/* This file was generated by SableCC (http://www.sablecc.org/). */

package soot.jimple.parser.node;

import java.util.*;
import soot.jimple.parser.analysis.*;

public final class AEnumModifier extends PModifier
{
    private TEnum _enum_;

    public AEnumModifier()
    {
    }

    public AEnumModifier(
        TEnum _enum_)
    {
        setEnum(_enum_);

    }
    public Object clone()
    {
        return new AEnumModifier(
            (TEnum) cloneNode(_enum_));
    }

    public void apply(Switch sw)
    {
        ((Analysis) sw).caseAEnumModifier(this);
    }

    public TEnum getEnum()
    {
        return _enum_;
    }

    public void setEnum(TEnum node)
    {
        if(_enum_ != null)
        {
            _enum_.parent(null);
        }

        if(node != null)
        {
            if(node.parent() != null)
            {
                node.parent().removeChild(node);
            }

            node.parent(this);
        }

        _enum_ = node;
    }

    public String toString()
    {
        return ""
            + toString(_enum_);
    }

    void removeChild(Node child)
    {
        if(_enum_ == child)
        {
            _enum_ = null;
            return;
        }

    }

    void replaceChild(Node oldChild, Node newChild)
    {
        if(_enum_ == oldChild)
        {
            setEnum((TEnum) newChild);
            return;
        }

    }
}
